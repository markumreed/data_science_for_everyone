from faker import Faker
import pandas as pd
import random 

fake = Faker()
Faker.seed(42)

profile = [fake.profile() for _ in range(100)]
df = pd.DataFrame(profile)
df['age'] = [random.randrange(18, 65, 1) for i in range(100)]
df.to_json("profiles.json")
df.to_csv("profiles.csv", index=False)
df.to_csv("profiles.tsv",sep="\t", index=False)



def to_xml(df):
    def row_xml(row):
        xml = ['<item>']
        for i, col_name in enumerate(row.index):
            xml.append('  <{0}>{1}</{0}>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)
    res = '\n'.join(df.apply(row_xml, axis=1))
    return(res)
1
with open('profiles.xml', 'w') as f:
    f.write(to_xml(df))






