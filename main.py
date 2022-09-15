import wget
import os.path

def get_protein_fasta(protein_list):
    for protein_id in protein_list:
        mono_file_path = "/home/mnguyen/alphafold_mono_fasta/%s.fasta" % (protein_id)
        if not os.path.exists(mono_file_path):
            URL = "https://rest.uniprot.org/uniprotkb/%s.fasta" % (protein_id)

            # download the fasta monomer file
            wget.download(URL, "/home/mnguyen/alphafold_mono_fasta")

            # concatanate the monomer file
            with open("/home/mnguyen/alphafold_mono_fasta/%s.fasta" % (protein_id)) as file:
                # data =""
                # lines = file.read().split('\n')
                # data += lines[0]
                # data += '\n'
                # data += "".join(lines[1:])
                data = file.read()
            data += data

            # write to a new file
            with open("/home/mnguyen/alphafold_homo_fasta/%s.fasta" % (protein_id), 'w') as file:
                file.write(data)
        else:
            print("File %s already exist" % (protein_id))

def get_cas9_fasta(protein_dict_with_cas9):
    for protein in protein_dict_with_cas9:
        cas9_id = protein_dict_with_cas9[protein]
        cas9_path = "/home/mnguyen/alphafold_cas9_fasta/%s.fasta" % (cas9_id)
        if not os.path.exists(cas9_path):
            URL = "https://rest.uniprot.org/uniprotkb/%s.fasta" % (cas9_id)

            # download the fasta cas9 file
            wget.download(URL, "/home/mnguyen/alphafold_cas9_fasta")
        else:
            print("File %s already exist" % (cas9_id))

def create_hetero(protein_dict_with_cas9):
    for protein_id in protein_dict_with_cas9:
        cas9_id = protein_dict_with_cas9[protein_id]
        with open("/home/mnguyen/alphafold_homo_fasta/%s.fasta" % (protein_id)) as file:
            data = file.read()
        with open("/home/mnguyen/alphafold_cas9_fasta/%s.fasta" % (cas9_id)) as file2:
            data2 = file2.read()
        data3 = data + data2

        file_path = "/home/mnguyen/alphafold_hetero_fasta/%s_%s.fasta" % (protein_id, cas9_id)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(data3)
        else:
            print("File already exist")


if __name__ == "__main__":
    protein_list = ["A0A142X169", "A0A142WY31", "A0A517U1U2", "A0A517U1I5", "A0A2W4MKW0", "A0A0B8YAX9",
                    "A0A350V0L1", "A0A838CTC1", "A0A1G8ZP20", "A0A6N4TLR5", "A0A6N7QZV0", "A0A150L959"]

    # a protein dictionary as the protein ID is the key and cas9 is the value
    protein_dict_with_cas9 = {"A0A142X169": "A0A142WV29", "A0A142WY31": "A0A142WV29", "A0A517U1U2": "A0A517TX54",
                    "A0A517U1I5": "A0A517TX54", "A0A2W4MKW0": "A0A1V5NU01", "A0A0B8YAX9": "A0A0B8YC59",
                    "A0A350V0L1": "A0A1V6I2Y8", "A0A838CTC1" : "A0A838CYB6", "A0A1G8ZP20" : "A0A1G9C575",
                    "A0A6N4TLR5" : "A0A6N4TLZ5", "A0A6N7QZV0" : "A0A6N7QXE6", "A0A150L959": "A0A150KLZ9"}
    # Download fasta file from the internet
    # get_protein_fasta(protein_list)

    # Download cas9 fasta file from the internet
    # get_cas9_fasta(protein_dict_with_cas9)

    # Make hetero dimer file
    create_hetero(protein_dict_with_cas9)

    print("Done")