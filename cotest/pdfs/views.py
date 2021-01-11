from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# Create your views here.


def genpdf(request):
    render(request,'ticket.html')
#     html_string = render_to_string('ticket.html')
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'r')
#         response.write(output.read())

#     return response