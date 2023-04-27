/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package Pecas;

import Auxiliar.Consts;
import Xadrez.Jogo;
import Xadrez.Tabuleiro;
import Auxiliar.Posicao;
import java.awt.Graphics2D;
import java.io.IOException;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

/**
 *
 * @author Junio
 */
public abstract class Peca {
    protected ImageIcon iImage;
    protected Posicao pPosicao;
    /* O elemento deve saber em qual cenário ele está */
    protected Tabuleiro tTabuleiro;

    protected Peca(String sAFileName, Posicao aPosicao) {
        this.pPosicao = aPosicao;
        try {
            iImage = new ImageIcon(new java.io.File(".").getCanonicalPath() + Consts.PATH + sAFileName);
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void setTabuleiro(Tabuleiro aTabuleiro) {
        this.tTabuleiro = aTabuleiro;
    }

    public void autoDesenho() {
        iImage.paintIcon(tTabuleiro, (Graphics2D) tTabuleiro.getGraphics(),
                pPosicao.getColuna() * Consts.SIZE, pPosicao.getLinha() * Consts.SIZE);
    }

    public boolean foiClicada(Posicao aPosicao) {
        return this.pPosicao.igual(aPosicao);
    }

    public Posicao getPosicao() {
        return pPosicao;
    }
}
