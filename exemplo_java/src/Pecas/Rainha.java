package Pecas;

import auxiliar.Posicao;

public class Rainha extends Peca{
    public Rainha(String sAFileName, Posicao aPosicao, boolean bBrancas) {
        super(sAFileName, aPosicao, bBrancas);
    }
    public String toString(){
        return "Rainha";
    }
    public boolean setPosicao(Posicao umaPosicao) {
        throw new UnsupportedOperationException("Implemente esta funcao para a " + this); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }    
}
