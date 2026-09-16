def testfn3(Pop):
    """
    Python verzia pôvodnej MATLAB funkcie testfn3.

    MATLAB logika:
        Fit(i) = sum_{j=1..lstring} ( -x_ij * sin(sqrt(abs(x_ij))) )

    Vstup:
        Pop:
            - 2D: tvar (lpop, lstring)
            - 1D: tvar (lstring,) -> interpretuje sa ako 1 jedinec
            - ND (>=3D): tvar (lpop, d2, d3, ...)
              -> lstring = d2*d3*...
              -> interne sa sploští na (lpop, lstring)

    Výstup:
        - 1D NumPy pole tvaru (lpop,)
          Fitness hodnota pre každého jedinca.
    −4189.829
    """
    import numpy as np

    Pop = np.asarray(Pop, dtype=float)

    if Pop.ndim == 1:
        # 1D pole interpretujeme ako jedného jedinca s N génmi
        lpop = 1
        lstring = Pop.shape[0]
        X = Pop.reshape(1, lstring)
    else:
        # Prvý rozmer = počet jedincov
        # Ostatné rozmery = gény jedinca
        lpop = Pop.shape[0]
        lstring = int(np.prod(Pop.shape[1:]))
        X = Pop.reshape(lpop, lstring)

    # --- Výpočet fitness ---
    Fit = np.sum(
        -X * np.sin(np.sqrt(np.abs(X))),
        axis=1
    )

    return Fit
