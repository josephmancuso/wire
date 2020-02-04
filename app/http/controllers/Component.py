from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from jinja2 import Markup
import json
import copy

class Component:


    def __init__(self, request: Request, view: View):
        """LivewireController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        self.view = view
        self.props = self.request.input('data', {})
        # self.properties.update(self.get_livewire_properties())
        self.view.share({'component': self.helper})
    
    def helper(self, component):
        template = self.view.render(f'livewire.{component}', self.get_livewire_properties()).rendered_template
        template = template.replace("<div>", f"""<div x-component='{component}' v-html="props.html" x-data='{component}()' x-init='init()'>""")
        template = template.replace("method=", "@click='handle($event)' method=")
        template += """
    <script>
        function METHOD_NAME() {
            return {
                component: null,
                props: {},
                init() {
                    this.component = this.$el.getAttribute('x-component')
                    axios.post('/livewire/props/'+this.component, {'data': this.props})
                        .then(response => {
                            this.$el.innerHTML = response.data
                            this.props = JSON.parse(response.headers['x-livewire'])
                        })
                    console.log(this.$el)
                },
                handle(event) {
                    console.log(this.props)
                    let method = event.target.getAttribute('method')
                    axios.post('/livewire/props/'+this.component, {'data': this.props, method: method})
                        .then(response => {
                            this.$el.innerHTML = response.data
                            this.props = JSON.parse(response.headers['x-livewire'])
                            console.log('and we are at', this.props)
                        })
                },
            }
        }
    </script>
        """
        template = template.replace('METHOD_NAME', component)
        print('data props is', self.get_livewire_properties())
        template = template.replace('DATA_PROPS', json.dumps(self.get_livewire_properties()))
        return Markup(template)
    
    def render(self, template):
        self.set_properties()

        print(self)
        if hasattr(self, self.request.input('method', '')):
            getattr(self, self.request.input('method'))()

        # Modified state now
        props = {}
        for prop in self.attrs:
            props.update({prop: self.__dict__.get(prop)})

        print('props1', props)
        print('ajax rendering', template, 'with', props)
        x = self.view.render(template, props).rendered_template
        x = x.replace("method=", "@click='handle($event)' method=")
        self.request.cookie('livewire:props', json.dumps(props))
        self.request.header('X-Livewire', json.dumps(props))
        print('template is', x)
        return x

    def set_properties(self):
        self.__dict__.update(self.request.input('data', {}))

    def get_livewire_properties(self):
        new_dict = {}
        for attribute, value in self.properties.items():
            new_dict.update({attribute: self.__dict__.get(attribute)})

        return new_dict
