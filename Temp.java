import java.util.Scanner;
import java.awt.datatransfer.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.awt.Toolkit;

public class Temp {

	@SuppressWarnings("finally")
	public static void main(String[] args) throws IOException {
		String sub = "ASW_SWITCH";
		File loc = new File(
				"C:\\Users\\swaraj_somala\\OneDrive - AVIN Systems Private Limited\\application.h\\ModeSwitch\\Rte_"
						+ sub + ".h");
		FileWriter fstream = new FileWriter(loc, true);
		BufferedWriter out = new BufferedWriter(fstream);
		Scanner one = new Scanner(System.in);
		while (true) {
			try {
				System.out.println("Enter String:");
				String str = one.next();
				String s = "#define " + str + " " + str.substring(0, str.indexOf("_", str.indexOf("_") + 1)) + "_" + sub
						+ str.substring(str.indexOf("_", str.indexOf("_") + 1));
				out.write(s);
				out.newLine();

			} catch (Exception e) {
				out.close();
				one.close();
				break;
			}
		}
		System.out.println("/*******************complete***************************************/");
		// while (true) {
		// String sub = "ASW_IRV_WRITE";
		//// System.out.println(s);
		// StringSelection stringSelection = new StringSelection(s+"\n");
		// Clipboard clpbrd = Toolkit.getDefaultToolkit().getSystemClipboard();
		// clpbrd.setContents(stringSelection, null);
	}
}
