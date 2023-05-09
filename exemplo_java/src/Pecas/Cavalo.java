package Pecas;

import auxiliar.Posicao;

public class Cavalo extends Peca{

    public Cavalo(String sAFileName, Posicao aPosicao, boolean bBrancas) {
           super(sAFileName, aPosicao, bBrancas);
    }
    public String toString(){
        return "Cavalo";
    }
    public boolean setPosicao(Posicao umaPosicao) {
        throw new UnsupportedOperationException("Implemente esta funcao para o " + this); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }    
}
