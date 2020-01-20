import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        sub_dataset = os.path.split(xml_file)[-1][:-4]
        dataset = root.get('name')
        for frame in root.findall('frame'):
            frame_number = str(frame.get('number'))
            for person in frame.findall('person'):
                value = (dataset,sub_dataset,frame_number ,person.get('id') )
                xml_list.append(value)
           
    column_name = ['dataset', 'sub_dataset' ,'frame_number', 'id']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
   
    image_path = r'C:\Users\yeop\Dropbox\lab\lab_beautifulsoup\groundtruth'
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('chokepoint_labels.csv', index=None)
    print('Successfully converted xml to csv.')

if __name__ == "__main__":
    main()
