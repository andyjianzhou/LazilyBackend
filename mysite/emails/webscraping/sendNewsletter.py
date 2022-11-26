from . import getNewsletter
from django.template.loader import render_to_string

def send_newsletter():
    links, titles = getNewsletter.get_newsletter()
    #create template
    template = """
    <html>
    <head>
    <style>
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    """
    template += "</style></head><body>"
    template += "<table style='width:100%'>"
    template += "<tr><th>Links</th><th>Titles</th></tr>"
    for i in range(len(links)):
        template += "<tr><td>" + links[i] + "</td><td>" + titles[i] + "</td></tr>"
    template += "</table></body></html>"
    return template