class OwnDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, val in dict(*args, **kwargs):
            self.__setitem__(key, val)


own_dict = OwnDict()
own_dict[4] = 1
own_dict[2] = 0.5
print(own_dict)


class OwnList(list):
    def __setitem__(self, index, value):
        list.append(self, value)

    def append(self, value):
        list.__setitem__(self, value)




own_list = OwnList()
own_list.append(3)
