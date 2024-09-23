import yaml
import pandas as pd
import torch
from oml.models.vit.vit import ViTExtractor
from oml.inference.flat import inference_on_images
from oml.registry.transforms import get_transforms_for_pretrained
from oml.utils.misc_torch import pairwise_dist
from oml.transforms.images.torchvision import get_normalisation_resize_torch
from oml.inference.flat import inference_on_dataframe
from oml.retrieval.postprocessors.pairwise import PairwiseImagesPostprocessor
from pprint import pprint


class IrisIdent:
    def __init__(self,cfg_yaml_path: str='iris.yaml'):
        with open(cfg_yaml_path, errors='ignore') as f:
             opt = yaml.safe_load(f)
             #print(opt)
        self.modeltype=opt['modeltype'] #|| 'vits16_dino'
        self.arch=opt['arch'] #|| 'vits16'
        self.weights=opt['weights']
        self.df_path=opt['df_path']      # pacients data iris embedding and ids in .csv
        self.imgsz=opt['imgsz'] #|| 128   # input size for model
        self.top_k=3
        pass


    # Load model
    def load_model(self):
        device = torch.device("cpu")
        self.model=ViTExtractor(weights=self.weights,arch=self.arch, normalise_features=False)
        #self.model = torch.load(self.weights,map_location=lambda storage, loc: storage)
        #self.model = model.cpu().double()
        self.model.eval()
        self.transform = get_normalisation_resize_torch(im_size=self.imgsz)
        #self.transform, _ = get_transforms_for_pretrained(self.modeltype)
        pass

    def get_data(self):
        dfall=pd.read_csv(self.df_path)
        df=dfall[dfall['split']=='validation']
        self.queries = df[df["is_query"]==1.0]["path"].tolist()
        self.galleries = df[df["is_gallery"]==1.0]["path"].tolist()
        self.lquery = df[df["is_query"]==1.0]["label"].tolist()
        self.lgallery = df[df["is_gallery"]==1.0]["label"].tolist()

    def calc_predict(self):
        args = {"num_workers": 0, "batch_size": 8}
        # эмбеддинги запросов и галереи
        self.features_queries = inference_on_images(self.model, paths=self.queries, transform=self.transform, **args)
        self.features_galleries = inference_on_images(self.model, paths=self.galleries, transform=self.transform, **args)
        # евклидово расстояние между ними - то есть по строкам расстояния галерей от фиксированного запроса
        from sklearn.neighbors import NearestNeighbors
        knn = NearestNeighbors(algorithm="auto", p=2)
        knn.fit(self.features_galleries)
        dists, ii_closest = knn.kneighbors(self.features_queries, n_neighbors=self.top_k, return_distance=True)
        self.dists=[]
        for d in dists:
          self.dists.append(d[0]) 
        print(self.dists)
        self.closest=[]
        for ii in ii_closest:
          self.closest.append(ii[0]) 
        print(self.closest)

    def infer(self):
        s=''
        for i in range(len(self.lquery)):
            ii=self.closest[i]
            m = self.dists[ii]
            if (self.lquery[i]!=self.lgallery[ii]):
                s = "Error: "
            else:
                s='Match:'

            print(s,'N query',i,' closest to:',ii,'distance:',m)
            print(s,'query   label:',str(self.lquery[i]),'path: ',self.queries[i])
            print(s,'predict label:',self.lgallery[ii],'path: ',self.galleries[ii])
            print('\n')


pass
