import re
import chardet
import xml.etree.ElementTree as ET
import pandas as pd
from io import StringIO

# 파일 경로
di_file_path = '../data/di_u.conf'
file_path = '../data/nc_doc_1_1.1'

def preprocessing(text):
    # 개행문자 제거
    print(type(text))
    print(text)
    text = re.sub('\\\\n', ' ', text)
    print(text)
    # 특수문자 제거
    # 특수문자나 이모티콘 등은 때로는 의미를 갖기도 하지만 여기에서는 제거했습니다.
    # text = re.sub('[?.,;:|\)*~`’!^\-_+<>@\#$%&-=#}※]', '', text)
    # 한글, 영문, 숫자만 남기고 모두 제거하도록 합니다.
    # text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', text)

    # 한글, 영문만 남기고 모두 제거하도록 합니다.
    # text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)

    # 중복으로 생성된 공백값을 제거합니다.
    text = re.sub(' +', ' ', text)

    return text

# 불용어 제거
def remove_stopwords(text):
    tokens = text.split(' ')
    stops = ['수', '현', '있는', '있습니다', '그', '년도', '합니다', '하는',
             '및', '제', '할', '하고', '더', '대한', '한', '그리고', '월',
             '저는', '없는', '입니다', '등', '일', '많은', '이런', '것은',
             '왜','같은', '같습니다', '없습니다', '위해', '한다']
    meaningful_words = [w for w in tokens if not w in stops]
    return ' '.join(meaningful_words)

def load_di_u_conf(file_path):
    with open(file_path, 'r') as file:
        tree = ET.parse(file_path)
        di_def = tree.getroot()

        # 모든 name 가져오기
    return [str(di_info.get('name')) for di_info in di_def.findall('DiInfo')]

# 빈 리스트 생성

# 파일을 열고 한 줄씩 읽기
def load_rdata(di_u_conf_path, file_path):
    keys = load_di_u_conf(di_u_conf_path)
    rdata = []
    with open(file_path, 'rb') as file:
        for line in file:
            # 줄 끝의 개행 문자 제거하고 널문자로 분리하여 리스트로 변환

            #line 인코딩 검출
            #result = chardet.detect(line)
            #encoding = result['encoding']
            #print(encoding)

            #print(line.count(b'\0'))

            items = line.split(b'\0')
            #print(len(row))

            # row 인코딩 검출
            #result = chardet.detect(row[0])
            #encoding = result['encoding']
            #print(encoding)

            #rdata.append([byte.decode('ISO-8859-1').strip() for byte in row])

            row_dict = {}
            for idx, item in enumerate(items):
                row_dict[keys[idx]] = item.decode('EUC-KR').strip()
                # print(idx, item)

                #print(keys[idx],)
            # rdata.append([byte.decode('EUC-KR').strip() if isinstance(byte, bytes) else str(byte, "EUC-KR").strip() for byte in row])
            rdata.append(row_dict)
            # print(type(row))
    return rdata


#print(columns)
#df = pd.DataFrame(load_rdata(file_path), columns=load_di_u_conf(di_file_path))
#print(df[['ntt_sj']].head())

#df = pd.DataFrame(load_rdata(di_file_path, file_path))
#print(len(df), df.shape)
#print(df[['ntt_sj']].head())
