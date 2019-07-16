import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Temp {
	public static void main(String[] args) throws IOException, InterruptedException {
		
		File[] files = new File(
				"E:\\checkout\\avin\\branches\\SWCCodeGenerator\\Testing\\1.0.3\\TestResult\\NonFunctionalTestCases")
						.listFiles();
		for (File file : files) {
			//TimeUnit.SECONDS.sleep(2);
			if (file.isFile()) {

				String sub = file.getName();
				File loc = new File(
						"E:\\checkout\\avin\\branches\\SWCCodeGenerator\\Testing\\1.0.3\\TestResult\\NonFunctionalTestCases\\"
								+ sub);
				String sub1 = sub.replaceAll(".c", "");
				final Scanner scanner = new Scanner(loc);
				String name = "Port";
				String str = null;
				while (scanner.hasNextLine()) {
					String lineFromFile = scanner.nextLine();
					if (lineFromFile.contains(name)) {
						str = lineFromFile.substring(lineFromFile.indexOf("= ") + 1, lineFromFile.indexOf("("));
						File loc1 = new File("E:\\temp\\nonfunctional\\Rte_" + sub1 + ".h");
						// File loc1 = new File(
						// "C:\\Users\\swaraj_somala\\OneDrive - AVIN Systems
						// Private
						// Limited\\application.h\\ModeSwitch\\Rte_"
						// + sub + ".h");
						FileWriter fstream = new FileWriter(loc1, true);
						BufferedWriter out = new BufferedWriter(fstream);
						String s = "#define " + str + " " + str.substring(0, str.indexOf("_", str.indexOf("_") + 1))
								+ "_" + sub1 + str.substring(str.indexOf("_", str.indexOf("_") + 1));
						out.write(s);
						out.write("\n");
						out.newLine();
						out.close();

					}
				}
				scanner.close();
			}
		}
	}
	//

	// Scanner one = new Scanner(System.in);
	// ArrayList<String> results = new ArrayList<String>();
	// File[] files = new File("C:\\Users\\swaraj_somala\\OneDrive - AVIN
	// Systems Private Limited\\application.h")
	// .listFiles();
	// // If this pathname does not denote a directory, then listFiles()
	// // returns null.
	// for (File file : files) {
	// if (file.isFile()) {
	// results.add(file.getName());
	// }
	// System.out.println(file.getName());
	// }
	// System.out.println("/*******************complete***************************************/");
	// while (true) {
	// String sub = "ASW_IRV_WRITE";
	//// System.out.println(s);
	// StringSelection stringSelection = new StringSelection(s+"\n");
	// Clipboard clpbrd = Toolkit.getDefaultToolkit().getSystemClipboard();
	// clpbrd.setContents(stringSelection, null);
}
