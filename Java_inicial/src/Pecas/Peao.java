/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package Pecas;

import Auxiliar.Consts;
import auxiliar.Posicao;
import java.awt.Graphics2D;
import java.io.IOException;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

/**
 *
 * @author Junio
 */
public class Peao extends Peca {
    public Peao(String sAFileName, Posicao aPosicao) {
        super(sAFileName, aPosicao);
    }
    public void MoveUp(){
        this.pPosicao.setLinha(this.pPosicao.getLinha()-1);
    }
    public void MoveDown(){
        this.pPosicao.setLinha(this.pPosicao.getLinha()+1);
    }
    public void MoveRight(){
        this.pPosicao.setColuna(this.pPosicao.getColuna()+1);
    }
    public void MoveLeft(){
        this.pPosicao.setColuna(this.pPosicao.getColuna()-1);
    }
}