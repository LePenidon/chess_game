/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Xadrez;

import Auxiliar.Consts;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JPanel;

/**
 *
 * @author junio
 */
public class Tabuleiro extends JPanel {

  @Override // sobrescrita do metodo paintComponent da classe JPanel
  protected void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g;
    /* 64 é o numedo de quadrantes de um tabuleiro de xadrez */
    for (int i = 0; i < 8; i++) {
      for (int j = 0; j < 8; j++) {
        if ((j + i) % 2 == 0)
          g2d.setColor(Color.lightGray);
        else
          g2d.setColor(Color.gray);
        g2d.fillRect(j * Consts.SIZE, i * Consts.SIZE,
            Consts.SIZE, Consts.SIZE);
      }
    }
  }
}