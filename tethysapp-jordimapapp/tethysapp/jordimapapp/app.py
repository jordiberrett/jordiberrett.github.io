from tethys_sdk.base import TethysAppBase, url_map_maker


class Jordimapapp(TethysAppBase):
    """
    Tethys app class for Jordi Map App.
    """

    name = 'Jordi - Map App'
    index = 'jordimapapp:home'
    icon = 'jordimapapp/images/icon2.png'
    package = 'jordimapapp'
    root_url = 'jordimapapp'
    color = '#010356'
    description = 'This is Jordi&#39;s Unique Map App to be hosted on Github.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='jordimapapp',
                controller='jordimapapp.controllers.home'
            ),
            UrlMap(
                name='map_view',
                url='jordimapapp/map_view',
                controller='jordimapapp.controllers.map_view'
            ),
            UrlMap(
                name='data_services',
                url='jordimapapp/data_services',
                controller='jordimapapp.controllers.data_services'
            ),
            UrlMap(
                name='about',
                url='jordimapapp/about',
                controller='jordimapapp.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='jordimapapp/proposal',
                controller='jordimapapp.controllers.proposal'
            ),
            UrlMap(
                name='wireframes',
                url='jordimapapp/wireframes',
                controller='jordimapapp.controllers.wireframes'
            ),
        )

        return url_maps
