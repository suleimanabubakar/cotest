from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# Create your views here.
import os

dirname = os.path.dirname(__file__)

# def genpdf(request):
#     # return render(request,'ticket.html')
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


def genpdf(request):
    # Make a PDF straight from HTML in a string.
    html = render_to_string('ticket.html')

    pdf = HTML(string=html).write_pdf()

    if os.path.exists(dirname):

        f = open(os.path.join(dirname, 'mypdfs.pdf'), 'wb')
        f.write(pdf) 
        
        # f.open(pdf)
        # os.startfile(dirname+'d.pdf',"print")
        
        


    return JsonResponse({'msg':'Success'})