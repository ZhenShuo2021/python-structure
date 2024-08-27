# 絕對導入
from src.package import module1
from src.package.utils import util
print("module2 start: ", __name__)
print("module2 end")

# 相對導入
# from .utils import util
# from . import module1
# print("module2 start: ", __name__)
# print("module2 end")

if __name__ == "__main__":
    print("module2 private part")