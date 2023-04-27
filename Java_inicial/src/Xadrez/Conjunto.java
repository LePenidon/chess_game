/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Xadrez;

import Pecas.Peca;
import auxiliar.Posicao;
import java.util.ArrayList;
/**
 *
 * @author junio
 */
public class Conjunto extends ArrayList<Peca>{
    public Conjunto(){
        super();
    }
    public void AutoDesenho(){
        for(int i = 0; i < this.size(); i++)
            this.get(i).autoDesenho();
    }
    public Peca getPecaClicada(Posicao aPosicao){
        for(int i = 0; i < this.size(); i++)
            if(this.get(i).foiClicada(aPosicao))
                return this.get(i);
        return null;
    }
    public void pecaFora(Peca aPeca){
        for(int i = 0; i < this.size(); i++)
            if(this.get(i) == aPeca)
                this.remove(i);
    }
}