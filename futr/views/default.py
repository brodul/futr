from pyramid.view import view_config

import futr.parsers


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    pivnica_aggregator = futr.parsers.PivnicaAggregator()
    try:
        pivnica_content = pivnica_aggregator.get_day_content()
    except futr.parsers.NoMenuForTodayError:
        pivnica_content = ""
    piramida_aggregator = futr.parsers.PiramidaAggregator()
    try:
        piramida_content = piramida_aggregator.get_day_content()
    except futr.parsers.NoMenuForTodayError:
        piramida_content = ""
    siska_aggregator = futr.parsers.SiskaAggregator()
    siska_content = siska_aggregator.get_weekly_content()
    return {'union': pivnica_content, 'piramida': piramida_content, 'siska': siska_content}
