from pyramid.view import view_config

import futr.parsers
from futr.controller.person_location import PersonLocationController


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    person_location_c = PersonLocationController()
    if request.method == 'POST':
        person = request.POST['name']
        location = request.POST['locationSelect']
        person_location_c.create_person_location(person, location)

    pivnica_aggregator = futr.parsers.PivnicaAggregator()
    try:
        pivnica_content = pivnica_aggregator.get_day_content()
    except futr.parsers.NoMenuForTodayError:
        pivnica_content = ""
    try:
        piramida_aggregator = futr.parsers.PiramidaAggregator()
        piramida_content = piramida_aggregator.get_day_content()
    except (futr.parsers.NoMenuForTodayError, ValueError):
        piramida_content = ""
    person_location = person_location_c.get()
    locations = person_location_c.get_locations()
    return {'union': pivnica_content, 'piramida': piramida_content,
        'locations': locations, 'person_locations': person_location}
