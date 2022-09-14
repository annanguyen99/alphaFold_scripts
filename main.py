import wget
import os.path

def get_fasta(protein_list):
    for protein_id in protein_list:
        mono_file_path = "/home/mnguyen/alphafold_mono_fasta/%s.fasta" % (protein_id)
        if not os.path.exists(mono_file_path):
            URL = "https://rest.uniprot.org/uniprotkb/%s.fasta" % (protein_id)

            # download the fasta monomer file
            wget.download(URL, "/home/mnguyen/alphafold_mono_fasta")

            # concatanate the monomer file
            with open("/home/mnguyen/alphafold_mono_fasta/%s.fasta" % (protein_id)) as file:
                data = file.read()
            data += data

            # write to a new file
            with open("/home/mnguyen/alphafold_homo_fasta/%s.fasta" % (protein_id), 'w') as file:
                file.write(data)
        else:
            print("File already exist")

def create_hetero(protein_list, cas9_list):
    print("Create hetero_file")
if __name__ == "__main__":
    protein_list = ["A0A142X169", "A0A142WY31", "A0A517U1U2", "A0A517U1I5", "A0A2W4MKW0", "A0A0B8YAX9",
                    "A0A350V0L1", "A0A838CTC1", "A0A1G8ZP20", "A0A6N4TLR5", "A0A6N7QZV0", "A0A150L959"]
    cas9_list = ["A0A142WV29", "A0A517TX54", ]
    get_fasta(protein_list)
    print("Done")