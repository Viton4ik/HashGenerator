import hashlib

# set input and outpun files
input_file = "passwords.txt"
output_file = "password_hashes.txt"

# main function
def main():
    # open source file with passwords and create an output file
    with open(input_file, "r") as f, open(output_file, "w") as out:
        for line in f:
            # generate hashed view for the passwords (one line -> one password)
            password = line.strip().encode("utf-8")
            hashed_password = hashlib.sha256(password).hexdigest()
            out.write(hashed_password + "\n")
        
if __name__ == '__main__':
    main()
