import gradio as gr
import requests
backend_url="https://res-backend-8hho.onrender.com"

def resumerequest(skills):
    response = requests.post(backend_url,json={"skills": skills})
    if response.status_code == 200:
        return response.json()["resume"]
    else:
        return "Error connecting to backend."

demo = gr.Interface(fn=resumerequest,inputs=gr.Textbox(label="Enter Skills", lines=5),outputs=gr.Textbox(label="Generated Resume", lines=20))
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
