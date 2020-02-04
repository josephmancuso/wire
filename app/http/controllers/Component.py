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
        template = template = f"""<div x-component='{component}' v-html="props.html" x-data='{component}()' x-init='init()'><div x-html="html"></div></div>"""
        template = template.replace("method=", "@click='handle($event)' method=")
        template += """
    <script>
        function METHOD_NAME() {
            return {
                component: null,
                html: null,
                props: DATA_PROPS ,
                init() {
                    console.log('calling init again')
                    this.component = this.$el.getAttribute('x-component')
                    axios.post('/livewire/props/'+this.component, {'data': this.props})
                        .then(response => {
                            this.html = response.data
                            this.props = JSON.parse(response.headers['x-livewire'])
                        })
                    console.log(this.props)
                },
                handle(event) {
                    console.log(this.props)
                    let method = event.target.getAttribute('method')
                    axios.post('/livewire/props/'+this.component, {'data': this.props, method: method})
                    .then(response => {
                            this.html = response.data
                            this.props = JSON.parse(response.headers['x-livewire'])
                        })
                },
            }
        }
    </script>
        """
        props = {}
        for prop in self.attrs or []:
            props.update({prop: self.__dict__.get(prop, 'NA')})

        template = template.replace('METHOD_NAME', component)

        template = template.replace('DATA_PROPS', json.dumps(props))
        print(self)
        print('props are', props)
        # print('component rendered template is', template)
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
        props = {}
        if not hasattr(self, 'attrs'):
            return props

        for prop in self.attrs or []:
            props.update({prop: self.__dict__.get(prop)})

        return props
