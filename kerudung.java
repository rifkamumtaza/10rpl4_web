import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class kerudung {
    public static void main(String[] args) {
        int menu = 0;
        int jawabanUser = 0;
        int totalHarga = 0;
        int jumlahBarang = 0;
        int uang = 0;

        JTextArea barang = new JTextArea(20, 30);
        barang.setText("=======HIJAB BY REGITA=======\n\n");
        barang.append("TERSEDIA\t:\n\n");
        barang.append("1. Segiempat Paris Jadul\t\tRp.20.000\n");
        barang.append("2. Segiempat Paris Premium\t\tRp.25.000\n");
        barang.append("3. Segiempat Bella Square\t\tRp.15.000\n");
        barang.append("4. Segiempat Plain Square\t\tRp.19.000\n");
        barang.append("5. Pashmina Silk\t\tRp.45.000\n");
        barang.append("6. Pashmina Ceruty\t\tRp.22.000\n");
        barang.append("7. Pashmina kaos\t\tRp.29.000\n");
        barang.append("8. Pashmina plisket\t\tRp.25.000\n");
        barang.append("9. Pashmina Shimmer\t\tRp.35.000\n");
        barang.append("10. Pashmina Shawl\t\tRp.50.000\n");
        barang.append("11. Bergo Hamidah\t\tRp.21.000\n");
        barang.append("0. Selesai\n\n");
        barang.append("Silahkan Pilih Menu Diatas (Inputkan Nomer)");

        JScrollPane tersedia = new JScrollPane(barang);

        do {
            menu = Integer.parseInt(JOptionPane.showInputDialog(null, tersedia, "MENU", JOptionPane.PLAIN_MESSAGE));
        
            switch (menu) {
                case 1:
                    int jadul = Integer.parseInt(JOptionPane.showInputDialog(null, "Segiempat Paris Jadul = Rp.20.000\n\nMau beli Segiempat Paris Jadul Berapa?", "SEGIEMPAT PARIS JADUL", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += jadul;
                    totalHarga += jadul * 20000;
                    break;

                case 2:
                    int prem = Integer.parseInt(JOptionPane.showInputDialog(null, "Segiempat Paris Premium = Rp.25.000\n\nMau Beli Segiempat Paris Premium Berapa?", "SEGIEMPAT PARIS PREMIUM", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += prem;
                    totalHarga += prem * 25000;
                    break;

                case 3:
                    int bel = Integer.parseInt(JOptionPane.showInputDialog(null, "Segiempat Bella Square = Rp.15.000\n\nMau Beli Segiempat Bella Square Berapa?", "SEGIEMPAT BELLA SQUARE", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += bel;
                    totalHarga += bel * 15000;
                    break;
                    
                case 4:
                    int pln = Integer.parseInt(JOptionPane.showInputDialog(null, "Segiempat Plain Square = Rp.19.000\n\nMau Beli Segiempat Plain Square Berapa?", "SEGIEMPAT PLAIN SQUARE", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += pln;
                    totalHarga += pln * 19000;
                    break;
                    
                case 5:
                    int slk = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Silk = Rp.45.000\n\nMau Beli Pashmina Silk Berapa?", "PASHMINA SILK", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += slk;
                    totalHarga += slk * 45000;
                    break;

                case 6:
                    int cr = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Ceruty = Rp.22.000\n\nMau Beli Pashmina Ceruty Berapa?", "PASHMINA CERUTY", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += cr;
                    totalHarga += cr * 22000;
                    break;

                case 7:
                    int ks = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Kaos = Rp.29.000\n\nMau Beli Pashmina Kaos Berapa?", "PASHMINA KAOS", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += ks;
                    totalHarga += ks * 29000;
                    break;

                case 8:
                    int pls = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Plisket = Rp.25.000\n\nMau Beli Pashmina Plisket Berapa?", "PASHMINA PLISKET", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += pls;
                    totalHarga += pls * 25000;
                    break;

                case 9:
                    int shm = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Shimmer = Rp.35.000\n\nMau Beli Pashmina Shimmer Berapa?", "PASHMINA SHIMMER", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += shm;
                    totalHarga += shm * 35000;
                    break;

                case 10:
                    int shw = Integer.parseInt(JOptionPane.showInputDialog(null, "Pashmina Shawl = Rp.50.000\n\nMau Beli Pashmina Shawl Berapa?", "PASHMINA SHAWL", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += shw;
                    totalHarga += shw * 50000;
                    break;

                case 11:
                    int BG = Integer.parseInt(JOptionPane.showInputDialog(null, "Bergo Hamidah = Rp.21.000\n\nMau Beli Bergo Hamidah Berapa?", "BERGO HAMIDAH", JOptionPane.QUESTION_MESSAGE));
                    jumlahBarang += BG;
                    totalHarga += BG * 21000;
                    break;

                case 0:
                    if (totalHarga > 0){
                        jawabanUser = JOptionPane.showConfirmDialog(null, "MENU SELESAI !!!\n\nBelanjaan Anda:\nRp." + totalHarga + "\n\nKembali Belanja?", "SELESAI !!!", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE);
                        break;
                    } else {
                        jawabanUser = JOptionPane.showConfirmDialog(null, "MENU SELESAI !!!\n\nAnda Belum Membeli Apapun !!!\n\nKembali Belanja?", "SELESAI !!!", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE);
                        break;
                    }             
                
                default:
                    if (totalHarga > 0){
                        jawabanUser = JOptionPane.showConfirmDialog(null, "Menu yang Anda Inputkan Tidak Tersedia !!!\n\nBelanjaan Anda:\nRp." + totalHarga + "\n\nLanjut Belanja?", "NO ITEM", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE);
                        break;
                    } else {
                        jawabanUser = JOptionPane.showConfirmDialog(null, "Menu yang Anda Inputkan Tidak Tersedia !!!\n\nANDA BELUM BERBELANJA APAPUN !!!\n\nLanjut Belanja?", "NO ITEM", JOptionPane.YES_NO_OPTION, JOptionPane.WARNING_MESSAGE);
                    }
                }

                if (menu >= 1 && menu <= 11){
                    jawabanUser = JOptionPane.showConfirmDialog(null, "Belanjaan Anda:\nRp." + totalHarga + "\n\nIngin Belanja Lagi?", "PILIHAN", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
                }

        } while (jawabanUser != JOptionPane.NO_OPTION);

        
        if (totalHarga == 0){
            JOptionPane.showMessageDialog(null, "Anda Tidak Berbelanja Apapun :(", "TIDAK BERBELANJA", JOptionPane.PLAIN_MESSAGE);
        } else {
            do {
                uang = Integer.parseInt(JOptionPane.showInputDialog(null, "Total Belanjaan Anda \nRp." + totalHarga + "\n\nMasukkan Nominal Uang", "UANG", JOptionPane.PLAIN_MESSAGE));
            
                if (uang < totalHarga){
                    JOptionPane.showMessageDialog(null, "Uang Anda kurang silahkan bayar dengan uang pas atau lebih", "UANG KURANG", JOptionPane.WARNING_MESSAGE);
                }

            } while (uang < totalHarga);

            int kembalian = uang - totalHarga;
            JOptionPane.showMessageDialog(null, "Kembalian Anda \nRp." + kembalian);

            JOptionPane.showMessageDialog(null, "=====HIJAB BY REGITA=====\n\nDetail Belanjaan Anda ===>\n\nBanyak Barang  : " + jumlahBarang + "\nHarga Total         : Rp." + totalHarga + "\n\nTotal Bayar          : Rp." + uang + "\nUang Kembalian : Rp." + kembalian + "\n\nTerimakasih sudah berbelanja\nSilahkan datang kembali\n\nKeluhan Hubungi : 0882009057369\n\n=====HIJAB BY REGITA=====", "NOTA", JOptionPane.PLAIN_MESSAGE);
        }
    }}