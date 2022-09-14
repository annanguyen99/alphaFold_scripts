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

if __name__ == "__main__":
    protein_list = ["A0A142X169"]
    get_fasta(protein_list)
    print("Done")