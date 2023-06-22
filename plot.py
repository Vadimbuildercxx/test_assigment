import pandas as pd
import matplotlib.pyplot as plt
import os

from pandas.plotting import scatter_matrix

class GraphPlotter():
    def __init__(self, folder="plots", json_path="https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json") -> None:
        self.df = pd.read_json(json_path)
        self.folder = folder

    def draw_plots(self):

        paths = []

        if not os.path.exists(self.folder):
            os.mkdir(os.path.join(os.getcwd(), self.folder))

        true_values = self.df[self.df.rb_corners == self.df.gt_corners].rb_corners.count()
        false_values = self.df[self.df.rb_corners != self.df.gt_corners].rb_corners.count()
        print(true_values, false_values)
        plt.bar(["true_values", "false_values"], [true_values, false_values])
        plt.ylabel("Number of samples")
        plt.title("Compare true and false preds")
        path_comp = os.path.join(os.getcwd(), self.folder, 'comarision.png') 
        paths.append(path_comp)
        plt.savefig(path_comp)
        plt.show()
        plt.close()

        df_clear = self.df.drop(['rb_corners', 'name'], axis=1)
        scatter_matrix(df_clear, figsize=(12, 12))
        path_scatter = os.path.join(os.getcwd(), self.folder, 'scatter_matrix.png') 
        paths.append(path_scatter)
        plt.savefig(path_scatter)
        plt.show()
        plt.close()

        fig, ax = plt.subplots(3, 3, figsize=(10, 10))
        fig.text(0.5, 0.04, 'Corners', ha='center')
        fig.text(0.04, 0.5, 'Quantity', va='center', rotation='vertical')
        for index, column in enumerate(df_clear[["mean","max","min",	"floor_mean", "floor_max", "floor_min", "ceiling_mean",	"ceiling_max", "ceiling_min"]]):
            sub = plt.subplot(3, 3, index+1)
            df_clear.boxplot(column = column, by = 'gt_corners', ax= sub, flierprops = dict(markerfacecolor = 'g',  linestyle = "none", markeredgecolor='none', alpha=0.25))
            plt.xlabel("")

        path_boxplots= os.path.join(os.getcwd(), self.folder, 'boxplots.png') 
        paths.append(path_boxplots)
        plt.savefig(path_boxplots)
        plt.show()
        plt.close()
        return paths

if __name__ == "__main__":
    plotter = GraphPlotter(folder="plots")
    plotter.draw_plots() 