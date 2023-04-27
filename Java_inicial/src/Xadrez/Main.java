/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Xadrez;

import Pecas.Peao;
import Auxiliar.Posicao;

/**
 *
 * @author junio
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                Jogo tMeuJogo = new Jogo();
                tMeuJogo.addPeca(new Peao("Peao.png", new Posicao(6, 0)), Jogo.CoresConjuntos.BRANCAS);
                tMeuJogo.addPeca(new Peao("Peao.png", new Posicao(6, 1)), Jogo.CoresConjuntos.BRANCAS);
                tMeuJogo.addPeca(new Peao("Peao.png", new Posicao(6, 2)), Jogo.CoresConjuntos.BRANCAS);
                tMeuJogo.addPeca(new Peao("Peao.png", new Posicao(6, 3)), Jogo.CoresConjuntos.BRANCAS);
                tMeuJogo.setVisible(true);
                tMeuJogo.go();
            }
        });
    }
}
