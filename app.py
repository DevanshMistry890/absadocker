from pyabsa import available_checkpoints
import warnings
warnings.simplefilter("ignore")
checkpoint_map = available_checkpoints('atepc', show_ckpts=False)
from pyabsa import ATEPCCheckpointManager
aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='english',
                                   auto_device=False  # False means load model on CPU
                                   )

import gradio as gr
import pandas as pd
def inference(text):
    result = aspect_extractor.extract_aspect(inference_source=[text],
                                             pred_sentiment=True)

    result = pd.DataFrame({
        'aspect': result[0]['aspect'],
        'sentiment': result[0]['sentiment']
    })

    return result

if __name__ == '__main__':
    iface = gr.Interface(
        fn=inference,
        inputs=["text"],
        examples=[['The wine list is incredible and extensive and diverse , the food is all incredible and the staff was all very nice ,'
                   ' good at their jobs and cultured .'],
                  ['Though the menu includes some unorthodox offerings (a peanut butter roll, for instance), the classics are pure and '
                   'great--we have never had better sushi anywhere, including Japan.'],
                  ['Everything, from the soft bread, soggy salad, and 50 minute wait time, with an incredibly rude service to deliver'
                   ' below average food .'],
                  ['Even though it is running Snow Leopard, 2.4 GHz C2D is a bit of an antiquated CPU and thus the occasional spinning '
                   'wheel would appear when running Office Mac applications such as Word or Excel .'],
                  ['Good Work user'],
                  ['camera is good, battery drains fast'],
                  ],
        outputs="dataframe",
        description="Project by Devansh Mistry with PyABSA Library",
        title='ASPECT BASED SEMANTICS ANALYTICS'
    )

    iface.launch()