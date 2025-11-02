# hello/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse(
        """
        <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background-color: #f0f2f5;
                    }
                    .message {
                        padding: 20px;
                        background-color: white;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                </style>
            </head>
            <body>
                <div class="message">
                    <h1>Hello!</h1>
                    <p>This is the CI/CD deployment test on Digital Ocean Cloud Proof of Concept</p>
                </div>
            </body>
        </html>
        """
    )