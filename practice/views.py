from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import google.generativeai as genai
from django.conf import settings

# Configure Gemini API (ensure you have set GEMINI_API_KEY in settings.py)
genai.configure(api_key=settings.GEMINI_API_KEY)

def compiler_page(request):
    """Renders the compiler page"""
    return render(request, "compiler.html")

def run_code(request):
    """Runs Python code and returns the output"""
    if request.method == "POST":
        code = request.POST.get("code", "")
        if not code:
            return JsonResponse({"error": "No code provided."})

        try:
            # Execute Python code
            process = subprocess.run(
                ["python", "-c", code],
                capture_output=True,
                text=True,
                timeout=5
            )
            output = process.stdout
            error = process.stderr
            if error:
                return JsonResponse({"error": error})
            return JsonResponse({"output": output})
        except subprocess.TimeoutExpired:
            return JsonResponse({"error": "Execution timed out."})
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"})
    return JsonResponse({"error": "Invalid request method."})

def optimize_code(request):
    """Gets optimization suggestions and optimized code"""
    if request.method == "POST":
        code = request.POST.get("code", "")
        if not code:
            return JsonResponse({"error": "No code provided."})

        try:
            # Use Gemini API for optimization suggestions
            prompt1 = f"Optimize this Python code and provide the optimal solution for this code I need only code:\n\n{code}"
            prompt2 = f"Suggestion on how to optimize this python code to get optimal solution:\n\n{code}"
            model = genai.GenerativeModel("gemini-1.5-flash")

            response1 = model.generate_content(prompt1)
            
            response2 = model.generate_content(prompt2)

            if not response1 or not response1.text:
                return JsonResponse({"error": "No response from Gemini API."})
            
            if not response2 or not response2.text:
                return JsonResponse({"error": "No response from Gemini API."})

            # For now, assuming Gemini API returns the optimization suggestions as well as optimized code
            explanation = response1.text
            optimized_code = response2.text  # Just for example, you can customize this if needed.

            # Return as plain text
            return JsonResponse({
                "optimization": explanation,
                "optimized_code": optimized_code
            })

        except Exception as e:
            return JsonResponse({"error": f"An error occurred while processing the request: {str(e)}"})

    return JsonResponse({"error": "Invalid request method."})
