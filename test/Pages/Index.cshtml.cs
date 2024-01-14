using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.IO;
using System.Threading.Tasks;
using CsvHelper;
using Newtonsoft.Json;
using System.Globalization;
using System.Diagnostics;
using System.Net.Http.Json;
using Newtonsoft.Json.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace test.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        [BindProperty]
        public IFormFile? Upload { get; set; }

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {  
        }
        [BindProperty]
        public string Description { get; set; }

        [BindProperty]
        public string Task { get; set; }

        public async Task<IActionResult> OnPostUploadFileAsync()
        {
            if (Upload != null && Upload.Length > 0)
            {
                TempData["Message"] = "<span style='color: #30db5b;'>Uploaded:</span> File, description, and task Uploaded!</ br>";
                var filePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "uploads", Upload.FileName);

                using (var stream = new FileStream(filePath, FileMode.Create))
                {
                    await Upload.CopyToAsync(stream);
                }

                

                // Convert CSV to JSON
                var csvFilePath = filePath;  // Assuming Uploaded file is a CSV
                var jsonFilePath = Path.ChangeExtension(filePath, ".json");  // Change extension to .json

                using (var reader = new StreamReader(csvFilePath))
                using (var csv = new CsvReader(reader, CultureInfo.InvariantCulture))
                {
                    var records = csv.GetRecords<dynamic>().ToList();

                    // Serialize to JSON
                    var json = JsonConvert.SerializeObject(records, Formatting.Indented);

                    // Write JSON to file
                    System.IO.File.WriteAllText(jsonFilePath, json);
                }


                    //data extraction
                    string jsonFileContent = System.IO.File.ReadAllText(jsonFilePath);
                    JArray jsonArray = JArray.Parse(jsonFileContent);

                    
                    if (jsonArray.Count > 0)
                    {
                    //tabela
                    string firstObjectString = jsonArray[0].ToString();
                        string secondObjectString = jsonArray[1].ToString();
                        string triObjectString = jsonArray[1].ToString();
                        string cetObjectString = jsonArray[1].ToString();
                        string petObjectString = jsonArray[1].ToString();

                    string inputs = $"Data example:'{firstObjectString}', Description:'{Description}', Data Path:'{jsonFilePath}'";//task mora bit locen zarad py strukture
                    string jsonString = $"[\n{firstObjectString},\n{secondObjectString},\n{triObjectString},\n{cetObjectString},\n{petObjectString}\n]";

                    //prikaz tabele
                    TempData["JsonData"] = jsonString;

                    TempData["Message45"] = $"<p><span style='color: #30db5b;'>success: </span>{inputs}</br></p>";


                    //run script
                    string pythonScriptPath = "/Users/timzav/Desktop/test/print.py";


                    // Create process start info
                    ProcessStartInfo psi = new ProcessStartInfo
                    {
                        FileName = "/Users/timzav/miniconda3/bin/python",
                        Arguments = $"{pythonScriptPath} {inputs} {Task}",
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        UseShellExecute = false,
                        CreateNoWindow = true
                    };

                    // Start the process
                    using (Process process = new Process { StartInfo = psi })
                    {
                        process.Start();

                        string error;
                        //reading output and error streams
                        string output = process.StandardOutput.ReadToEnd();
                        error = process.StandardError.ReadToEnd();
                        process.WaitForExit();//wait for the process to finish
                        /*if (string.IsNullOrEmpty(error))
                        {
                            error = "none (running proccess {generate py})";
                        }*/
                        //nepotrebno
                        
                        TempData["Message2"] = $"<p><span style='color: #30db5b;'>success: </span>{output}</br><span style='color: #ff6961;'>error:</span>{error}</p>";

                    }
                    
                }
                else
                    {
                        Console.WriteLine("The JSON array is empty.");
                    }



                
        // END run script
            }
            else
            {
                TempData["Message"] = "<span style='color: #ff6961;'>ERROR:</span>ERROR: File, description, or task not uploaded!";
            }

            // Redirect back to the index page after the file is uploaded
            return RedirectToPage("/Index");
        }


    }

}
