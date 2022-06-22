from easydict import EasyDict as edict

__C = edict()
cfg = __C

# general parameters
__C.title = 'CS\u00b2: A Controllable and Simultaneous Synthesizer of Images and Annotations with Minimal Human Intervention'
__C.authors = {'Xiaodan Xing':'1',
               'Jiahao Huang':'1,5',
               'Yang Nan':'1',
               'Yinzhe Wu':'1,2',
              'Chenjia Wang':'3',
               'Zhifan Gao': '4',
                'Simon Walsh': '1',
                'Guang Yang':'1,5'}
__C.institutions = {'1':'National Heart and Lung Institute, Imperial College London, London, UK',
'2':'Department of Biomedical and Engineering, Imperial College London, London, UK',
'3':'Edinburgh Centre for Robotics, Heriot-Watt University, Edinburgh, UK',
'4':'School of Biomedical Engineering, Sun Yat-sen University, Guangdong, China',
'5':'Cardiovascular Research Centre, Royal Brompton Hospital, London, UK',
                    }

__C.abstract = 'The destitution of image data and corresponding expert annotations limit the training capacities of AI diagnostic models and potentially ' \
               'inhibit their performance. To address such a problem of data and label scarcity,' \
               ' generative models have been developed to augment the training datasets. Previously proposed generative ' \
               'models usually require manually adjusted annotations (e.g., segmentation masks) or need pre-labeling. ' \
               'However, studies have found that these pre-labeling based methods can induce hallucinating artifacts, ' \
               'which might mislead the downstream clinical tasks, while manual adjustment could be onerous and subjective. ' \
               'To avoid manual adjustment and pre-labeling, we propose a novel controllable and simultaneous synthesizer (dubbed CS\u00b2) ' \
               'in this study to generate both realistic images and corresponding annotations at the same time. Our CS\u00b2 model ' \
               'is trained and validated using high resolution CT (HRCT) data collected from COVID-19 patients to realize an efficient ' \
               'infections segmentation with minimal human intervention. Our contributions include 1) a conditional image synthesis network ' \
               'that receives both style information from reference CT images and structural information from unsupervised segmentation masks, ' \
               'and 2) a corresponding segmentation mask synthesis network to automatically segment these synthesized images simultaneously. ' \
               'Our experimental studies on HRCT scans collected from COVID-19 patients demonstrate that our CS\u00b2 model ' \
               'can lead to realistic synthesized datasets and promising segmentation results of COVID infections compared ' \
               'to the state-of-the-art nnUNet trained and fine-tuned in a fully supervised manner. '

__C.codelinks = ['https://github.com/ayanglab/CS2',#'code':
                 'https://github.com/ayanglab/CS2',#'arxiv':
                 './cite.txt']#'bibtex':

__C.method = 'The novelty of our work is three-fold: 1) we develop a novel unsupervised mask-to-image ' \
             'synthesis pipeline that generates images controllably without human labeling; ' \
             '2) instead of directly using the numeric and disarranged unsupervised segmentation masks, ' \
             'which are cluttered with over-segmented super-pixels, we assign the mean Hounsfield unit (HU) ' \
             'value for each cluster in the unsupervised segmentation masks to obtain an ordered and well-organized labeling; ' \
             'and 3) we propose a new synthesis network structure featured by multiple adaptive instance normalization ' \
             '(AdaIN) blocks that handles unaligned structural and tissue information.'
__C.graphabstract = './resources/fig1.png'

__C.results = {}

__C.results.item1 = {}
__C.results.item1.title = 'Example synthetic images from four generative models.'
__C.results.item1.filepath = './resources/fig4.png'
__C.results.item1.caption = 'The masks are synthetic segmentation masks that corresponded with these images. Red pixels indicate lung tissues and green pixels are GGOs. ' \
                            'We also include synthetic samples of different modalities in our supplementary file.'
__C.results.item1.type = 'figure'

# __C.results.item2 = {}
# __C.results.item2.title = 'Test'
# __C.results.item2.filepath = './resources/table1.xlsx'
# __C.results.item2.caption = ' '
# __C.results.item2.type = 'table'

__C.results.item2 = {}
__C.results.item2.title = 'The synthetic images of our model are structurally editable'
__C.results.item2.filepath = './resources/fig6.png'
__C.results.item2.caption = 'An example of our synthetic images (b) structurally edited with the Unsupervised masks (a) ' \
                            'by adding circular patches of different HU values (1-4) and radii (5-8). ' \
                            'The patches in (a1) to (a4) have a radius of 30 pixels, and the patches in (a1) to (a4) have a mean HU value of -600'
__C.results.item2.type = 'figure'

__C.results.item3 = {}
__C.results.item3.title = 'Applications on brain MRI'
__C.results.item3.filepath = './resources/figS8.png'
__C.results.item3.caption = 'Our V2M2I model can synthesize four modalities at the same time, as well as their segmentation results. Fig. 5 is a typical failed cases with scattering wrongly segmented pixels with 8% wrongly segmented pixels. Post-processing algorithms such as connected component analysis, can remove these scatters. '
__C.results.item3.type = 'figure'

__C.results.item4 = {}
__C.results.item4.title = 'Applications on lung fibrosis HRCT'
__C.results.item4.filepath = './resources/figS7.png'
__C.results.item4.caption = 'The HRCT appearance of IPF is more complex than GGO and consolidation. We trained a synthesizer on UIP cases only, and inferenced the UIP synthesizer with non-UIP HRCT images. As is shown, by improving the class number of unsupervised guidance maps, we can successfully model the appearance of IPF as well as controllably synthesize IPF CT images.'
__C.results.item4.type = 'figure'