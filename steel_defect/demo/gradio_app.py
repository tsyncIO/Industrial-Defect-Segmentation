import gradio as gr
from steel_defect.inference import Predictor

def create_demo(predictor):
    def predict(image):
        prediction = predictor.predict(image)
        return prediction
        
    interface = gr.Interface(
        fn=predict,
        inputs=gr.Image(),
        outputs=gr.Image(),
        title="Steel Defect Detection"
    )
    return interface

def launch_gradio(model_path):
    predictor = Predictor(model_path)
    interface = create_demo(predictor)
    interface.launch()