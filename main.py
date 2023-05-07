from tqdm import trange

for i in trange(10 ** 9, total=float("inf")):
    for j in trange(10 ** 6, leave=False, desc=f'iter{i}'):
    #     for k in trange(10 ** 6):
    #         pass
        pass