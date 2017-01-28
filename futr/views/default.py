from pyramid.view import view_config

import futr.parsers


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    pivnica_parser = futr.parsers.PivnicaParser()
    try:
        pivnica_content = pivnica_parser.get_day_content()
    except futr.parsers.NoMenuForTodayError:
        pivnica_content = ""
    return {'union': pivnica_content}
