from torchvision.models import resnet34
import torch.nn as nn
from torch import load, device
import torchvision.transforms as transforms
from PIL import Image
import requests
from io import BytesIO
import torch

class idmodel:
    def __init__(self):
        model = resnet34()
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, 114)
        dev = device("cpu")
        model.to(dev)
        model.load_state_dict(load('/home/juanruedz/Desktop/PlanB myshroom/myshroomweights114.pth',map_location=torch.device('cpu')))
        model.eval()
        self.mod = model
    def predict (self, url):
        data_transforms = transforms.Compose([
                transforms.Resize((150,150)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        dicti = {'Agaricus_augustus': 0,
        'Agaricus_campestris': 1,
        'Agaricus_xanthodermus': 2,
        'Amanita_augusta': 3,
        'Amanita_bisporigera': 4,
        'Amanita_calyptroderma': 5,
        'Amanita_citrina': 6,
        'Amanita_flavoconia': 7,
        'Amanita_flavorubens': 8,
        'Amanita_fulva': 9,
        'Amanita_jacksonii': 10,
        'Amanita_junquillea': 11,
        'Amanita_pantherina': 12,
        'Amanita_parcivolvata': 13,
        'Amanita_persicina': 14,
        'Amanita_phalloides': 15,
        'Amanita_rubescens': 16,
        'Amanita_vaginata': 17,
        'Amanita_velosa': 18,
        'Amanita_xanthocephala': 19,
        'Aureoboletus_betula': 20,
        'Aureoboletus_mirabilis': 21,
        'Aureoboletus_russellii': 22,
        'Baorangia_bicolor': 23,
        'Boletus_edulis': 24,
        'Boletus_reticulatus': 25,
        'Cantharellus_cibarius': 26,
        'Cantharellus_cinnabarinus': 27,
        'Cantharellus_formosus': 28,
        'Cantharellus_lateritius': 29,
        'Cerioporus_squamosus': 30,
        'Chalciporus_piperatus': 31,
        'Chlorophyllum_brunneum': 32,
        'Chlorophyllum_molybdites': 33,
        'Chlorophyllum_rhacodes': 34,
        'Clavulina_coralloides': 35,
        'Clavulina_rugosa': 36,
        'Craterellus_cornucopioides': 37,
        'Craterellus_fallax': 38,
        'Craterellus_tubaeformis': 39,
        'Cuphophyllus_pratensis': 40,
        'Cuphophyllus_virgineus': 41,
        'Exsudoporus_frostii': 42,
        'Fomes_fomentarius': 43,
        'Fomitopsis_betulina': 44,
        'Fomitopsis_mounceae': 45,
        'Fomitopsis_pinicola': 46,
        'Ganoderma_applanatum': 47,
        'Ganoderma_tsugae': 48,
        'Gliophorus_psittacinus': 49,
        'Grifola_frondosa': 50,
        'Harrya_chromipes': 51,
        'Hericium_americanum': 52,
        'Hericium_coralloides': 53,
        'Hericium_erinaceus': 54,
        'Hortiboletus_rubellus': 55,
        'Humidicutis_marginata': 56,
        'Hydnum_repandum': 57,
        'Hygrocybe_acutoconica': 58,
        'Hygrocybe_cantharellus': 59,
        'Hygrocybe_coccinea': 60,
        'Hygrocybe_conica': 61,
        'Hygrocybe_flavescens': 62,
        'Hygrocybe_singeri': 63,
        'Imleria_badia': 64,
        'Ischnoderma_resinosum': 65,
        'Laetiporus_cincinnatus': 66,
        'Laetiporus_gilbertsonii': 67,
        'Laetiporus_sulphureus': 68,
        'Leccinum_aurantiacum': 69,
        'Leccinum_scabrum': 70,
        'Leccinum_versipelle': 71,
        'Leucoagaricus_americanus': 72,
        'Leucoagaricus_leucothites': 73,
        'Leucocoprinus_birnbaumii': 74,
        'Leucocoprinus_cepistipes': 75,
        'Leucocoprinus_fragilissimus': 76,
        'Lichenomphalia_chromacea': 77,
        'Lichenomphalia_umbellifera': 78,
        'Macrolepiota_clelandii': 79,
        'Macrolepiota_procera': 80,
        'Meripilus_sumstinei': 81,
        'Merulius_tremellosus': 82,
        'Multiclavula_mucida': 83,
        'Neoboletus_erythropus': 84,
        'Other': 85,
        'Other_Agaricus_Species': 86,
        'Other_Amanita_Species': 87,
        'Other_Bolete_Species': 88,
        'Other_Cantharellus_Species': 89,
        'Other_Hygrocybe_Species': 90,
        'Other_Pleurotus_Species': 91,
        'Other_Shelf_Fungi_Species': 92,
        'Phaeolus_schweinitzii': 93,
        'Pleurotus_citrinopileatus': 94,
        'Pleurotus_levis': 95,
        'Pleurotus_ostreatus': 96,
        'Pleurotus_pulmonarius': 97,
        'Podaxis_pistillaris': 98,
        'Psilocybecubensis': 99,
        'Psilocybeovoideocystidiata': 100,
        'Retiboletus_ornatipes': 101,
        'Strobilomyces_strobilaceus': 102,
        'Suillellus_amygdalinus': 103,
        'Suillellus_luridus': 104,
        'Trametes_betulina': 105,
        'Trametes_coccinea': 106,
        'Trametes_gibbosa': 107,
        'Trametes_versicolor': 108,
        'Tylopilus_felleus': 109,
        'Tylopilus_plumbeoviolaceus': 110,
        'Tylopilus_rubrobrunneus': 111,
        'Xerocomellus_chrysenteron': 112,
        'Xerocomus_subtomentosus': 113}
        
        keys = dicti.values()
        values = dicti.keys()
        class_mapping = dict(zip(keys, values))
        resp= requests.get(url)
        img = Image.open(BytesIO(resp.content))
        clean_image = data_transforms(img)
        clean_image = torch.unsqueeze(clean_image,dim=0)
        prediction = self.mod(clean_image)
        predicted_index = int(prediction[0].argmax(0))
        predicted = class_mapping[predicted_index]
        print(predicted_index)
        return predicted