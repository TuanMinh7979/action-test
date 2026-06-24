from module_a import x


def main():
    print("Day la ham main() trong module_b.py")
    ket_qua = x()
    print(f"Gia tri tra ve tu ham x(): {ket_qua}")


if __name__ == "__main__":
    main()
