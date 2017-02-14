from pyramid.view import view_config

import futr.parsers


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
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
    return {'union': pivnica_content, 'piramida': piramida_content}
