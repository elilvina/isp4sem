import logging
logging.basicConfig(level=logging.INFO)

def main():
    logging.info("well, hello there.")
    name = input("what is your name? ")
    logging.info("it's nice to meet you, " + name + "!")
    age = input("how old are you? ")
    logging.info("wow, " + age + "! you are at the best age.")

if __name__=="__main__":
    main()
