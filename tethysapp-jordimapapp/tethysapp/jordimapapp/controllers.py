from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import TextInput
from tethys_sdk.gizmos import RangeSlider
from tethys_sdk.gizmos import LinePlot

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {

    }

    return render(request, 'jordimapapp/home.html', context)

def map_view(request):
    notes_input = TextInput(display_text='Consultant Notes',
                           name='consultant_notes',
                           placeholder='city code, known cut & fill depths, etc.',
                           prepend='Notes')

    slider1 = RangeSlider(display_text='Zoom',
                          name='slider1',
                          min=0,
                          max=100,
                          initial=50,
                          step=1)

    line_plot_view = LinePlot(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Cut and Fill',
        subtitle='measured in cubic feet',
        spline=True,
        x_axis_title='Horizontal Path',
        x_axis_units='mi',
        y_axis_title='Amount Removed',
        y_axis_units='ft^3',
        series=[
            {
                'name': 'Cut',
                'color': '#0066ff',
                'marker': {'enabled': False},
                'data': [
                    [0, 5], [10, 70],
                    [20, 86.5], [30, 66.5],
                    [40, 32.1],
                    [50, 12.5], [60, 47.7],
                    [70, 85.7], [80, 106.5]
                ]
            },
            {
                'name': 'Fill',
                'color': '#ff6600',
                'data': [
                    [0, 15], [10, 50],
                    [20, 56.5], [30, 46.5],
                    [40, 22.1],
                    [50, 2.5], [60, 27.7],
                    [70, 55.7], [80, 76.5]
                ]
            }
        ]
    )

    context = {'notes_input': notes_input,
               'slider1': slider1,
               'line_plot_view': line_plot_view
    }

    return render(request, 'jordimapapp/map_view.html', context)

def data_services(request):
    context = {

    }

    return render(request, 'jordimapapp/data_services.html', context)

def about(request):
    context = {

    }

    return render(request, 'jordimapapp/about.html', context)

def proposal(request):
    context = {

    }

    return render(request, 'jordimapapp/proposal.html', context)

def wireframes(request):
    context = {

    }

    return render(request, 'jordimapapp/wireframes.html', context)
