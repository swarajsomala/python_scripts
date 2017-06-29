import java.io.File;
public class CreationOfFolderRecursively {
	public static void main(String[] args) {
		CreationOfFolderRecursively obj = new CreationOfFolderRecursively();
		File file = new File("E:\\files\\");
		String[] names = file.list();
		String outputpath = "E:\\rec\\";
		for (String name : names) {
			String temp = "E:\\files\\" + name;
			obj.m1(temp, name, outputpath);
		}
	}
	void m1(String temp, String name, String outputpath) {
		try {
			if (new File(temp).isDirectory()) {
				new File(outputpath + "\\" + name).mkdirs();
				System.out.println(outputpath + "\\" + name + "   is created ");
				String[] names = new File(temp).list();
				for (String s : names) {
					m1(temp + "\\" + s, s, outputpath + "\\" + name);
				}
			}
		} catch (Exception e) {
		}

	}
}
