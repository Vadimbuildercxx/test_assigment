#### Link:
Download pandas json :
https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json
#### Task context:
These are deviations of floor vs ceiling corners of one of our models with ground truth labels
for the room name and number of corners in that room with predictions. Please create
meaningful statistics of how well the model performed.
#### Additional information:
Gt_corners = ground truth number of corners in the room
Rb_corners = number of corners found by the model
Mean max min and all others are deviation values in degrees.

#### Main tasks:
Create project in idea, pycharm or vscode

Create requirements.txt and virtual env

Create class for drawing plots

Create function “draw_plots”

→ reads json file passed as parameter as a pandas dataframe

→ draws plot for comparing different columns

→ saves plots in a folder called “plots”

→ returns paths to all plots


Create jupyter notebook called Notebook.ipynb in the root directory to call and visualize our
plots

Publish the project on github

Email us with link to your project