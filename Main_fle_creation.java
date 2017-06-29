import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Folders {
	public static void main(String[] args) throws IOException {
		int c = 0;
		File file = new File("E:\\files");
		// System.out.println(file.getParent());
		String[] names = file.list();
		for (String name : names) {
			if (new File("E:\\files\\" + name).isDirectory()) {
				// System.out.println("********************"+name+"**************************");
				File[] files = new File("E:\\files\\" + name).listFiles();
				for (File file1 : files) {
					if (file1.isFile()) {
						String sub = file1.getName();
						// System.out.println(sub);
						String sub1 = sub.replaceAll(".c", "");
						final Scanner scanner = new Scanner(file1);
						String name1 = "PORT";
						String str = null;
						while (scanner.hasNextLine()) {
							String lineFromFile = scanner.nextLine();
							if (lineFromFile.contains(name1)) {
								try {
									str = lineFromFile.substring(lineFromFile.indexOf("= ") + 1,
											lineFromFile.indexOf("("));
									new File("E:\\output\\" + name).mkdirs();
									File loc1 = new File("E:\\output\\" + name + "\\Rte_" + sub1 + ".h");
									FileWriter fstream = new FileWriter(loc1, true);
									BufferedWriter out = new BufferedWriter(fstream);
									String s = "#define " + str + " "
											+ str.substring(0, str.indexOf("_", str.indexOf("_") + 1)) + "_" + sub1
											+ str.substring(str.indexOf("_", str.indexOf("_") + 1));
									out.write(s);
									out.write("\n");
									out.newLine();
									out.close();
								} catch (Exception e) {
									System.out.println(c++);
								}
							}
						}
						scanner.close();

					}

				}

			}
		}
	}
}
