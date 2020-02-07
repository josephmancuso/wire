"""A LivewireProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.view import View
import json
from jinja2 import Markup

class LivewireProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        """Boots services required by the container."""
        self.view = view
        view.share({'component': self.helper})
    
    def helper(self, component):
        template = self.view.render(f'livewire.{component}').rendered_template
        wire_template = template.partition("<wire>")
        template = template = f"""
            <div x-component='{component}' v-html="props.html" x-data='{component}()' x-init='init()'>
                <div x-html="html"></div>
                {''.join(wire_template[1:])}
            </div>
        """
        template = template.replace("@method=", "@click='handle($event)' method=")
        template = template.replace("prop='", "x-model.lazy='props.")
        template = template.replace('prop="', 'x-model.lazy="props.')
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
                    axios.post('/livewire/props/'+this.component, {'data': this.props, method: 'mount'})
                        .then(response => {
                            this.html = response.data
                            console.log(response)
                            console.log(response.headers['x-livewire'])
                            this.props = JSON.parse(response.headers['x-livewire'])
                        })
                    console.log(this.props)
                },
                handle(event) {
                    console.log(this.props)
                    let method = event.target.getAttribute('method')
                    let send = event.target.getAttribute('x-send')
                    
                    axios.post('/livewire/props/'+this.component, {'data': this.props, method: method, 'send': send})
                    .then(response => {
                            this.html = response.data
                            this.props = JSON.parse(response.headers['x-livewire'])
                            if (response.headers['x-livewire-redirect']) {
                                window.location.replace(response.headers['x-livewire-redirect']);   
                            }
                        })
                },
            }
        }
    </script>
        """
        props = {}
        # for prop in self.attrs or []:
        #     props.update({prop: self.__dict__.get(prop, 'NA')})

        template = template.replace('METHOD_NAME', component)
        template = template.replace('template', 'div')

        template = template.replace('DATA_PROPS', json.dumps(props))
        # print(self)
        print('original rendered props props are',json.dumps(props))
        # print('component rendered template is', template)
        return Markup(template)
    