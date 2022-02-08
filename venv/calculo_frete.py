from frete import frete_inter, frete_nacio
class Calculo_Frete(object):
    def calcula(self, produto, frete):
        valor_com_frete = frete.calcula(produto)
        print(valor_com_frete)

if __name__ == '__main__':
    from produto import Produto
    calculo_frete = Calculo_Frete()
    produto = Produto(100)
    calculo_frete.calcula(produto,frete_nacio)
    calculo_frete.calcula(produto,frete_inter)
