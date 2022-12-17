with import <nixpkgs> { };

mkShell {
  nativeBuildInputs = [
    direnv
  ];
  buildInputs = [
    pkgs.python3
    pkgs.poetry
    pkgs.chromium
    pkgs.chromedriver
  ];
  NIX_ENFORCE_PURITY = true;
  shellHook = ''
  '';
}