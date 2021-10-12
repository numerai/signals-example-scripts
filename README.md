```
███████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██╗     ███████╗
██╔════╝██║██╔════╝ ████╗  ██║██╔══██╗██║     ██╔════╝
███████╗██║██║  ███╗██╔██╗ ██║███████║██║     ███████╗
╚════██║██║██║   ██║██║╚██╗██║██╔══██║██║     ╚════██║
███████║██║╚██████╔╝██║ ╚████║██║  ██║███████╗███████║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝
```

The official examples scripts for the [Signals](https://signals.numer.ai) Tournament

# Contents

- [Quick Start](#quick-start)
- [Next Steps](#next-steps)
  - [Data Pipeline](#data-pipeline)
  - [Modeling](#modeling)
  - [Automation](#automation)
- [FAQ](#faq)
- [Support](#support)

# Quick Start

```
pip install -U pip && pip install -r requirements.txt
python example_model.py
```

The example script model will produce a validation_predictions.csv file 
which you can upload at https://signals.numer.ai/tournament to get model diagnostics.

### TODO: gif here

If the current round is open (Saturday 18:00 UTC through Monday 14:30 UTC), you 
can submit your predictions and start getting results on live tournament data. You 
can create your submission by uploading the example_predictions.csv or generated tournament_predictions.csv 
file at https://signals.numer.ai/tournament

### TODO: gif here

# Next Steps
The example model is a good baseline model, but we can do much better. There are three
main paths for improving your Signals model: finding better data, improving your
features, and improving your modeling.

### Data pipeline
The `example_data_pipeline.py` script shows how we use the Open Signals package
to easily get pricing data and use it to create technical features.
[Open Signals](https://github.com/councilofelders/opensignals) is a repository created by 
the Numerai Council of Elders. The goal is to create a single source for users to get 
access to financial datasets and pre-made feature engineering.



### Modeling
TODO: what else should we say about modeling?
Check out the forums for in depth discussions on model research.

### Automation
You can upload your predictions directly to our [GraphQL API](https://api-tournament.numer.ai/) or through the [Python client](https://github.com/uuazed/numerapi/).

To access the API, you must first create your API keys in your [account page](https://numer.ai/account) and provide them to the client:

```python
import numerapi 

example_public_id = "somepublicid"
example_secret_key = "somesecretkey"
napi = numerapi.SignalsAPI(example_public_id, example_secret_key)
```

After instantiating the NumerAPI client with API keys, you can then upload your submissions programmatically:

```python
# upload predictions
model_id = napi.get_models()['your_model_name']
napi.upload_predictions("signals_yahoo.csv", model_id=model_id)
```

The recommended setup for a fully automated submission process is to use Numerai Compute. Please see the
[Numerai CLI documentation](https://github.com/numerai/numerai-cli) for instructions on how to deploy your
models to AWS.

# FAQ

# Support
If you need help or have any questions, please connect with us on our [community chat](http://community.numer.ai/) or [forums](https://forum.numer.ai/).

If something in this repo doesn't work, please [file an issue](https://github.com/numerai/signals-example-scripts/issues).