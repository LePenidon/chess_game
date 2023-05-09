package Xadrez;

import Auxiliar.Consts;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.image.BufferStrategy;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

public class Tabuleiro extends JPanel {

    Graphics g2;
    Jogo j;

    Tabuleiro() {
        j = null;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        /*64 é o numedo de quadrantes de um tabuleiro de xadrez*/
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if ((j + i) % 2 == 0) {
                    g2d.setColor(Color.lightGray);
                } else {
                    g2d.setColor(Color.gray);
                }
                g2d.fillRect(j * Consts.SIZE, i * Consts.SIZE,
                        Consts.SIZE, Consts.SIZE);
            }
        }
    }

}
