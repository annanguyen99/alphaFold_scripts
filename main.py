import wget

def get_fasta():

    URL = "https://rest.uniprot.org/uniprotkb/A0A142X169.fasta"

    repose = wget.download(URL, "/home/mnguyen/alphafold_fasta")

if __name__ == "__main__":
    get_fasta()