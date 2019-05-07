def Trilateration(R_1,R_2,R_3):
        x_1 = 0;x_2 = 2;x_3 = 4
        y_1 = 0;y_2 = 0;y_3 = 0        
        A_1 = (-2*x_1 + 2*x_2)
        B_1 = (-2*y_1 + 2*y_2)
        C_1 = (R_1*R_1) - (R_2*R_2) - (x_1*x_1) + (x_2*x_2) - (y_1*y_1) + (y_2*y_2)
        D_1 = (-2*x_2) + (2*x_3)
        E_1 = (-2*y_2) + (2*y_3)
        F_1 = (R_2*R_2) - (R_3*R_3) - (x_2*x_2) + (x_3*x_3) - (y_2*y_2) + (y_3*y_3)
        X = (C_1*E_1 - F_1*B_1)/(E_1*A_1 - B_1*D_1)
        Y = (C_1*D_1 - A_1*F_1)/(B_1*D_1 - A_1*E_1)
        return(X,Y)
