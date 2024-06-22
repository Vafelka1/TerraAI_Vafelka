import time
from iris_ident_knn3 import IrisIdent


class IrisIdentVitsDino(IrisIdent):
    def __init__(self,conf_path: str):
       super().__init__(conf_path)
       print("init success")
       pass


def main():
    I=IrisIdentVitsDino('iris.yaml')
    I.load_model()
    I.get_data()
    I.calc_predict()
    I.infer()
    exit(0)



if __name__ == "__main__":
    main()
